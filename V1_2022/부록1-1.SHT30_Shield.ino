/*
Date    : Nov-7, 2021
Book    : "라즈베리파이로 IoT 만들기"
Chapter : 부록 1
 - 예제코드 1
 - Wemos D1 Mini SHT30 Shield 실습
*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <WEMOS_SHT3X.h>

// 네트워크 설정
const char* ssid = "wifi_SSID";          //wifi SSID 기입
const char* password = "접속 암호";         //wifi 접속 암호 기입

// MQTT 설정
const char* mqtt_server = "192.168.219.205";  //MQTT IP 주소 기입
#define mqtt_user "test"     //MQTT Username
#define mqtt_password "test" //MQTT Password
#define temperature_topic "homenet/Sensor1/temperature"  //Topic temperature
#define humidity_topic "homenet/Sensor1/humidity"        //Topic humidity

// 객체 생성
SHT3X sht30(0x45);
WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;

#define MSG_BUFFER_SIZE	(50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

// 와이파이 접속
void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is active low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }
}

// MQTT 재연결
void reconnect() {
  while (!client.connected()) {
    Serial.print("Connetion a server MQTT...");
    if (client.connect("ESP8266Client", mqtt_user, mqtt_password)) {
      Serial.println("OK");
      Serial.println("");
    } else {
      Serial.print("NO, error : ");
      Serial.print(client.state());
      Serial.println("Wait 5 seconds before starting again");
      delay(5000);
    }
  }
}

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(9600);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  // MQTT 연결 유지
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // 온습도 값 출력
  if(sht30.get()==0){
    Serial.print("Temperature in Celsius : ");
    Serial.println(sht30.cTemp);
    Serial.print("Temperature in Fahrenheit : ");
    Serial.println(sht30.fTemp);
    Serial.print("Relative Humidity : ");
    Serial.println(sht30.humidity);
    Serial.println();
  }
  else
  {
    Serial.println("Error!");
  }

  unsigned long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    ++value;
    
    // 온습도값 발행
    client.publish(temperature_topic, String(sht30.cTemp).c_str(), true);   //Publish the temperature on topic_temperature_topic
    client.publish(humidity_topic, String(sht30.humidity).c_str(), true);   //And humidity  
  }

  delay(5000);
}
