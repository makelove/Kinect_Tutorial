#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

#include "cv.h"
#include "highgui.h"
#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <XnCppWrapper.h>
#include <time.h>

using namespace std;
using namespace cv;

int backproject_mode = 0;
int select_object = 0;
int track_object = 0;
int show_hist = 1;
int print_num=0;   //照片输出次序初始化

CvPoint origin;
CvRect selection;
CvRect track_window;
CvBox2D track_box;
CvConnectedComp track_comp;
CvPoint2D32f center,center_temp,center_temperater;

int hdims=16;
float hranges_arr[]={0,180};
float* hranges=hranges_arr;
int vmin=10,vmax=256,smin=30;

IplImage *image = 0, *hsv = 0, *hue = 0, *mask = 0, *backproject = 0, *histimg = 0;
CvHistogram *hist = 0;

//响应鼠标事件
void on_mouse(int event,int x,int y,int flags,void* param)
{
	if(!image)
		return;

	if(image->origin)
		y = image->height - y;

	if(select_object)
	{
		selection.x = MIN(x,origin.x);
		selection.y = MIN(y,origin.y);
		selection.width = selection.x + CV_IABS(x - origin.x);
		selection.height = selection.y + CV_IABS(y - origin.y);

		selection.x = MAX(selection.x,0);
		selection.y = MAX(selection.y,0);
		selection.width = MIN(selection.width,image->width);
		selection.height = MIN(selection.height,image->height);
		selection.width -= selection.x;
		selection.height -= selection.y;
	}

	switch(event)
	{
	case CV_EVENT_LBUTTONDOWN:
		origin = cvPoint(x,y);
		selection = cvRect(x,y,0,0);
		select_object = 1;
		break;
	case CV_EVENT_LBUTTONUP:
		select_object = 0;
		if(selection.width>0&&selection.height>0)
		{
			track_object = -1;
			center=cvPoint2D32f(0.0,0.0);
		}
		break;
	}
}

//OpenNI错误检查
void CheckOpenNIError(XnStatus eResult,string sStatus)
{
	if(eResult!=XN_STATUS_OK)
		cout<<sStatus<<"Error: "<<xnGetStatusString(eResult)<<endl;
}

int main(int argc, char** argv)
{
	XnStatus eResult=XN_STATUS_OK;
	xn::ImageMetaData imageMD;
	xn::DepthMetaData depthMD;

	//opencv
	IplImage* imgRGB8u=cvCreateImage(cvSize(640,480),IPL_DEPTH_8U,3);  
	IplImage* imageShow=cvCreateImage(cvSize(640,480),IPL_DEPTH_8U,3);  
	IplImage* imgDepth16u=cvCreateImage(cvSize(640,480),IPL_DEPTH_16U,1);  
	IplImage* depthShow=cvCreateImage(cvSize(640,480),IPL_DEPTH_8U,1);  
	//cvNamedWindow("depth",1);
	char key=0;
    CvFont font;
	cvInitFont(&font,CV_FONT_HERSHEY_DUPLEX ,1.0f,1.0f,0,1,CV_AA);

	//initial context
	xn::Context mContext;
	eResult=mContext.Init();
	CheckOpenNIError(eResult,"initial context");

	//create image generator
	xn::ImageGenerator mImageGenerator;
	eResult=mImageGenerator.Create(mContext);
	CheckOpenNIError(eResult,"Create image generator");

	//create depth generator
	xn::DepthGenerator mDepthGenerator;
	eResult=mDepthGenerator.Create(mContext);
	CheckOpenNIError(eResult,"Create depth generator");

	//set map mode
	XnMapOutputMode mapMode;
	mapMode.nXRes=640;
	mapMode.nYRes=480;
	mapMode.nFPS=15;
	eResult=mImageGenerator.SetMapOutputMode(mapMode);
	eResult=mDepthGenerator.SetMapOutputMode(mapMode);

	//correct view port    
	mDepthGenerator.GetAlternativeViewPointCap().SetViewPoint(mImageGenerator);   

	//start generate data
	eResult=mContext.StartGeneratingAll();
	eResult=mContext.WaitNoneUpdateAll();

	cout<< "Hot keys: \n"
		"\tESC or s - quit tracking\n"
		"To initialize tracking, select the object with mouse\n";

	cvNamedWindow("CamShift",1);
	cvMoveWindow("CamShift",400,200);
	cvSetMouseCallback("CamShift",on_mouse,0);//获取ROI区域

	while((key!=27)&&!(eResult= mContext.WaitNoneUpdateAll( )))
	{
		mImageGenerator.GetMetaData(imageMD);
		//mDepthGenerator.GetMetaData(depthMD);
		memcpy(imgRGB8u->imageData,imageMD.Data(),640*480*3);
		cvCvtColor(imgRGB8u,imageShow,CV_RGB2BGR);
		//memcpy(imgDepth16u->imageData,depthMD.Data(),640*480*2);  
		//cvConvertScale(imgDepth16u,depthShow,255/4096.0,0);  
		/*cvShowImage("depth",depthShow);
		cvMoveWindow("depth",700,200);*/
		int c;
		if( !imageShow )
			break;

		//分配空间
		if( !image )
		{
			image = cvCreateImage(cvGetSize(imageShow),8,3);
			image->origin = imageShow->origin;
			hsv = cvCreateImage(cvGetSize(imageShow),8,3);
			hue = cvCreateImage(cvGetSize(imageShow),8,1);
			mask = cvCreateImage(cvGetSize(imageShow),8,1);
			backproject = cvCreateImage(cvGetSize(imageShow),8,1);
			hist = cvCreateHist(1,&hdims,CV_HIST_ARRAY, &hranges,1);//创建直方图			
		}

		cvCopy(imageShow,image,0);
		cvCvtColor(image,hsv,CV_BGR2HSV);//转换到hsv颜色空间

		if(track_object!=0)
		{
			int _vmin = vmin, _vmax = vmax;

			//检查数组元素是否在两个数之间
			cvInRangeS(hsv, cvScalar(0,smin,MIN(_vmin,_vmax),0),cvScalar(180,256,MAX(_vmin,_vmax),0), mask);
			cvSplit(hsv, hue, 0, 0, 0); //分离hsv图像的三通道,获得H分量

			if( track_object < 0 )
			{
				float max_val = 0.f;
				cvSetImageROI(hue,selection);
				cvSetImageROI(mask,selection);
				cvCalcHist(&hue,hist,0, mask);
				cvGetMinMaxHistValue(hist,0,&max_val,0,0);//获取直方图的最大阈值
				cvConvertScale(hist->bins,hist->bins,max_val?255./max_val:0.,0);//使用线性变换转换数组 
				cvResetImageROI(hue);
				cvResetImageROI(mask);
				track_window = selection;
				track_object = 1;
			}

			cvCalcBackProject(&hue, backproject, hist);//计算hue的反向投影图
			cvAnd(backproject, mask, backproject, 0);//得到掩膜内的反向投影
			//camshift算法应用
			cvCamShift( backproject, track_window,cvTermCriteria(CV_TERMCRIT_EPS|CV_TERMCRIT_ITER,10,1),&track_comp, &track_box );
			track_window = track_comp.rect;//得到跟踪结果的矩形框

			if( image->origin )
				track_box.angle = -track_box.angle;

			//画出跟踪结果的位置
			cvEllipseBox(image,track_box,CV_RGB(255,0,0),1,CV_AA,0);
			//cvRectangle(image,cvPoint(track_window.x,track_window.y),cvPoint(track_window.x+track_window.width,track_window.y+track_window.height),CV_RGB(255,0,0),1,CV_AA,0);
			//对中心值赋值
			center=track_box.center;
			//cout<<"中心坐标为："<<"("<<center.x<<","<<center.y<<")"<<endl;
			 
			/*计算彩色图像投影到深度图像后的坐标（x,y），以及在该点的z值索引，
			根据这个索引可以找到该点在深度图像中的像素值，也即深度*/
			//实时计算并输出跟踪结果质心的三维坐标
	        XnPoint3D proP,realP;
			unsigned int idx;
			idx=center.y*640+center.x;//计算在深度图像上的索引
			proP.X=center.x;
			proP.Y=center.y;
			proP.Z=mDepthGenerator.GetDepthMap()[idx];//将单位由mm转换为m
			mDepthGenerator.ConvertProjectiveToRealWorld(1,&proP,&realP);

			if(realP.X==0||realP.Y==0||realP.Z==0)
				continue;
			cout<<"帧_"<<print_num<<"的三维坐标为："<<"("<<realP.X<<","<<realP.Y<<","<<realP.Z<<")"<<endl;
			Sleep(1000);//设置每一帧间停顿的时间
		}  

		if(select_object&&selection.width>0&&selection.height>0)//如果正处于物体选择，画出选择框
		{
			cvSetImageROI(image,selection);
			cvXorS(image,cvScalarAll(255),image,0);
			cvResetImageROI(image);
		}

		cvShowImage("CamShift",image);

		//保存每一帧视频画面
	    char frame_name[13];
		sprintf(frame_name, "%s%d%s", "帧_", print_num, ".jpg");//保存的图片名
        cvSaveImage(frame_name,image);   //保存一帧图片
		print_num++;
		c = cvWaitKey(1000);//设置帧间停顿的时间与输出三维坐标每帧间的间隔时间相同

		if((char) c == 'p')
			c=cvWaitKey(0);
		if((char) c == 27)
			break;
		if(((char) c) == 's')
		{
			track_object=0;
			break;
		}
	}
	//cvDestroyWindow("depth");
	cvDestroyWindow("CamShift");
	cvReleaseImage(&imgDepth16u); 
	cvReleaseImage(&imgRGB8u);  
	cvReleaseImage(&depthShow); 
	cvReleaseImage(&imageShow);  
	mContext.StopGeneratingAll();  
	mContext.Shutdown();  
	return 0;
}

