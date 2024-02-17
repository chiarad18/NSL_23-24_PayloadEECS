#include "soar_barometer.h"
SOAR_BAROMETER bmu;
void setup(){
   Serial.begin(115200);

  bmu.Initialize();

}
void loop(){
  float* accel = imu_sensor.GET_ACCELERATION();
  for(int i=0; i<3; i++){
    Serial.print("Accel array: ");
    Serial.print(accel[i]);
    Serial.print(" ");
  }
  Serial.print("\n");
  delay(2000);
}
