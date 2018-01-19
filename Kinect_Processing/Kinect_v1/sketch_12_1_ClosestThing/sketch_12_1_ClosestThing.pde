//不生效？

import org.openkinect.processing.*; //<>//

// Kinect Library object
Kinect kinect2;

float minThresh = 480;
float maxThresh = 830;
PImage img;

void setup() {
  size(512, 424);
  kinect2 = new Kinect(this);
  kinect2.initDepth();
  //kinect2.initDevice();
  img = createImage(kinect2.width, kinect2.height, RGB);
}


void draw() {
  background(0);

  img.loadPixels();

  PImage dImg = kinect2.getDepthImage();
  //image(dImg, 0, 0);

  // Get the raw depth as array of integers
  int[] depth = kinect2.getRawDepth();
  
  //int record = 4500;
  int record = kinect2.height;
  int rx = 0;
  int ry = 0;

  for (int x = 0; x < kinect2.width; x++) {
    for (int y = 0; y < kinect2.height; y++) {
      int offset = x + y * kinect2.width;
      int d = depth[offset];

      if (d > minThresh && d < maxThresh && x > 100 && y > 50) {
        img.pixels[offset] = color(255, 0, 150);
        
        if (y < record) {
          record = y;
          rx = x;
          ry = y;
        }
        
        
      } else {
        img.pixels[offset] = dImg.pixels[offset];
      }
    }
  }
  img.updatePixels();
  image(img,0,0);
  
  fill(255);
  ellipse(rx, ry, 32, 32);
}