import org.openkinect.processing.*; //<>//

Kinect kinect2;

void setup() {
  size(1024, 848, P2D);
  kinect2 = new Kinect(this);
  // Start all data
  kinect2.initVideo();
  kinect2.initDepth();
  //kinect2.initIR();
  //kinect2.initRegistered();
  //kinect2.initDevice();
}


void draw() {
  background(0);
  image(kinect2.getVideoImage(), 0, 0, kinect2.width*0.267, kinect2.height*0.267);
  image(kinect2.getDepthImage(), kinect2.width, 0);
  //image(kinect2.getIrImage(), 0, kinect2.height);

  //image(kinect2.getRegisteredImage(), kinect2.width, kinect2.height);
  fill(255);
  text("Framerate: " + (int)(frameRate), 10, 515);
}