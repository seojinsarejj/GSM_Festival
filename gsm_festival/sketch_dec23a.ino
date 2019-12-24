#include <Adafruit_NeoPixel.h>

#define PIN 2
#define NUM_LEDS 24
#define PUMP 13
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

int a = 0;
int i = 0;

void setup() {
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(PUMP,OUTPUT);
  strip.begin();
  strip.show();
}

void loop() {
  i = (i + 1) % 24;
  color(a);
      
  if(Serial.available()) {
    char c = Serial.read();
    
    if(c == '1'){
      a=1;
      digitalWrite(8,HIGH);
      delay(1000);
      digitalWrite(8,LOW);
    }
    else if(c == '2'){
      a=2;
      digitalWrite(8,HIGH);
      digitalWrite(9,HIGH);
      delay(1000);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
    }
    else if(c == '3'){
      a=3;
      digitalWrite(PUMP, HIGH);
      delay(1000);
      digitalWrite(PUMP, LOW);
    }
    else if(c == '0'){
      a=0;
    }
  }

  strip.show();
  delay(80);

}
int color(int a){
  if (a==0){
    //no
    strip.setPixelColor(i % 24, 0, 0, 0);
    strip.setPixelColor((i + 1) % 24, 0, 0, 0);
    strip.setPixelColor((i + 2) % 24, 0, 0, 0);
    strip.setPixelColor((i + 3) % 24, 0, 0, 0);
    strip.setPixelColor((i + 4) % 24, 0, 0, 0);
    strip.setPixelColor((i + 5) % 24, 0, 0, 0);
  }
  if (a==1){
    //초록
    strip.setPixelColor(i % 24, 0, 0, 0);
    strip.setPixelColor((i + 1) % 24, 0, 1, 0);
    strip.setPixelColor((i + 2) % 24, 0, 4, 0);
    strip.setPixelColor((i + 3) % 24, 0, 16, 0);
    strip.setPixelColor((i + 4) % 24, 0, 30, 0);
    strip.setPixelColor((i + 5) % 24, 0, 60, 0);
  }
    if (a==2){
    //파랑
    strip.setPixelColor(i % 24, 0, 0, 0);
    strip.setPixelColor((i + 1) % 24, 0, 0, 1);
    strip.setPixelColor((i + 2) % 24, 0, 0, 4);
    strip.setPixelColor((i + 3) % 24, 0, 0, 16);
    strip.setPixelColor((i + 4) % 24, 0, 0, 30);
    strip.setPixelColor((i + 5) % 24, 0, 0, 60);
  }
    if (a==3){
    //빨강
    strip.setPixelColor(i % 24, 0, 0, 0);
    strip.setPixelColor((i + 1) % 24, 1, 0, 0);
    strip.setPixelColor((i + 2) % 24, 4, 0, 0);
    strip.setPixelColor((i + 3) % 24, 16, 0, 0);
    strip.setPixelColor((i + 4) % 24, 30, 0, 0);
    strip.setPixelColor((i + 5) % 24, 60, 0, 0);
  }
}
