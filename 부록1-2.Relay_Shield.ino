/*
Date    : Nov-7, 2021
Book    : "라즈베리파이로 IoT 만들기"
Chapter : 부록 1
 - 예제코드 2
 - Wemos D1 Mini SHT30 Shield 실습
*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// 네트워크 설정
const char* ssid = "wifi_SSID";          //wifi SSID 기입
const char* password = "접속 암호";         //wifi 접속 암호 기입

// Relay 설정
const int relayPin = D1;                      //Relay Pin

// MQTT 설정
const char* mqtt_server = "192.168.219.205";  //MQTT IP 주소 기입
#define mqtt_user "test"     //MQTT Username
#define mqtt_password "test" //MQTT Password
#define switch_state_topic "homenet/Switch1/state"      //Topic switch 상태
#define switch_command_topic "homenet/Switch1/command"  //Topic switch 명령
//String switch_command

// 객체 생성
WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;

// 와이파이 접속
void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
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

String switch1;
String strTopic;
String strPayload;

void callback(char* topic, byte* payload, unsigned int length) {
 
  payload[length] = '\0';
  strTopic = String((char*)topic);
  if(strTopic == switch_command_topic)
    {
    switch1 = String((char*)payload);
    if(switch1 == "ON")
      {
        Serial.println("ON");
        client.publish(switch_state_topic,"ON");
        digitalWrite(relayPin, HIGH);
      }
    else
      {
        Serial.println("OFF");
        client.publish(switch_state_topic,"OFF");
        digitalWrite(relayPin, LOW);
      }
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
  Serial.begin(9600);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  pinMode(relayPin, OUTPUT);  //릴레이핀을 OUTPUT으로 설정
}

void loop() {
  // MQTT 연결 유지
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // 스위치 ON/OFF 명령수신
  client.subscribe(switch_command_topic);  
}
