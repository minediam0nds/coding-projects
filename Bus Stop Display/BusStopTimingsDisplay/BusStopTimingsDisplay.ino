#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <time.h>
#include <stdio.h>
#include <math.h>
#include <WiFiClientSecure.h>


#include <GxEPD2_BW.h>
#include <GxEPD2_3C.h>
#include <GxEPD2_4C.h>
#include <GxEPD2_7C.h>
#include <Fonts/FreeMonoBold24pt7b.h>
#include <Fonts/FreeMonoBold18pt7b.h>
#include <Fonts/FreeMonoBold12pt7b.h>
#include <Fonts/FreeMonoBold9pt7b.h>
#include "GxEPD2_display_selection_new_style.h"
#include <Fonts/FreeSans24pt7b.h>


//print busnumber:timings
//timings order 136p, 136a, 317i, 317o, 315i, 317o, 73a, 73t
//317 1 is int, 315 2 is int, 73 2 is to amk
const char* rootca = R"EOF(
-----BEGIN CERTIFICATE-----
MIIFiTCCA3GgAwIBAgIQb77arXO9CEDii02+1PdbkTANBgkqhkiG9w0BAQsFADBO
MQswCQYDVQQGEwJVUzEYMBYGA1UECgwPU1NMIENvcnBvcmF0aW9uMSUwIwYDVQQD
DBxTU0wuY29tIFRMUyBSU0EgUm9vdCBDQSAyMDIyMB4XDTIyMDgyNTE2MzQyMloX
DTQ2MDgxOTE2MzQyMVowTjELMAkGA1UEBhMCVVMxGDAWBgNVBAoMD1NTTCBDb3Jw
b3JhdGlvbjElMCMGA1UEAwwcU1NMLmNvbSBUTFMgUlNBIFJvb3QgQ0EgMjAyMjCC
AiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBANCkCXJPQIgSYT41I57u9nTP
L3tYPc48DRAokC+X94xI2KDYJbFMsBFMF3NQ0CJKY7uB0ylu1bUJPiYYf7ISf5OY
t6/wNr/y7hienDtSxUcZXXTzZGbVXcdotL8bHAajvI9AI7YexoS9UcQbOcGV0ins
S657Lb85/bRi3pZ7QcacoOAGcvvwB5cJOYF0r/c0WRFXCsJbwST0MXMwgsadugL3
PnxEX4MN8/HdIGkWCVDi1FW24IBydm5MR7d1VVm0U3TZlMZBrViKMWYPHqIbKUBO
L9975hYsLfy/7PO0+r4Y9ptJ1O4Fbtk085zx7AGL0SDGD6C1vBdOSHtRwvzpXGk3
R2azaPgVKPC506QVzFpPulJwoxJF3ca6TvvC0PeoUidtbnm1jPx7jMEWTO6Af77w
dr5BUxIzrlo4QqvXDz5BjXYHMtWrifZOZ9mxQnUjbvPNQrL8VfVThxc7wDNY8VLS
+YCk8OjwO4s4zKTGkH8PnP2L0aPP2oOnaclQNtVcBdIKQXTbYxE3waWglksejBYS
d66UNHsef8JmAOSqg+qKkK3ONkRN0VHpvB/zagX9wHQfJRlAUW7qglFA35u5CCoG
AtUjHBPW6dvbxrB6y3snm/vg1UYk7RBLY0ulBY+6uB0rpvqR4pJSvezrZ5dtmi2f
gTIFZzL7SAg/2SW4BCUvAgMBAAGjYzBhMA8GA1UdEwEB/wQFMAMBAf8wHwYDVR0j
BBgwFoAU+y437uOEeicuzRk1sTN8/9REQrkwHQYDVR0OBBYEFPsuN+7jhHonLs0Z
NbEzfP/UREK5MA4GA1UdDwEB/wQEAwIBhjANBgkqhkiG9w0BAQsFAAOCAgEAjYlt
hEUY8U+zoO9opMAdrDC8Z2awms22qyIZZtM7QbUQnRC6cm4pJCAcAZli05bg4vsM
QtfhWsSWTVTNj8pDU/0quOr4ZcoBwq1gaAafORpR2eCNJvkLTqVTJXojpBzOCBvf
R4iyrT7gJ4eLSYwfqUdYe5byiB0YrrPRpgqU+tvT5TgKa3kSM/tKWTcWQA673vWJ
DPFs0/dRa1419dvAJuoSc06pkZCmF8NsLzjUo3KUQyxi4U5cMj29TH0ZR6LDSeeW
P4+a0zvkEdiLA9z2tmBVGKaBUfPhqBVq6+AL8BQx1rmMRTqoENjwuSfr98t67wVy
lrXEj5ZzxOhWc5y8aVFjvO9nHEMaX3cZHxj4HCUp+UmZKbaSPaKDN7EgkaibMOlq
bLQjk2UEqxHzDh1TJElTHaE/nUiSEeJ9DU/1172iWD54nR4fK/4huxoTtrEoZP2w
AgDHbICivRZQIA9ygV/MlP+7mea6kMvq+cYMwq7FGc4zoWtcu358NFcXrfA/rs3q
r5nsLFR+jM4uElZI7xc7P0peYNLcdDa8pUNjyw9bowJWCZ4kLOGGgYz+qxcs+sji
Mho6/4UIyYOf8kpIEFR3N+2ivEC+5BB09+Rbu7nzifmPQdjH5FCQNYA+HLhNkNPU
98OwoX6EyneSMSy4kLGCenROmxMmtNVQZlR4rmA=
-----END CERTIFICATE-----
)EOF";


WiFiClientSecure client;

const char* nextbusarray[] = {
  "NextBus",
  "NextBus2",
  "NextBus3"
};

struct struct1 {
  const char* servicenum;
  int direction1;
  int direction2;
  int direction1count;
  int direction2count;
};

struct1 dict[] = {
  {"315", 5, 4, 0, 0},
  {"317", 3, 2, 0, 0},
  {"73", 7, 6, 0, 0}
};


const char* important2[] = {
  "315 TO S'GOON INT:",
  "317 TO S'GOON INT:"
};


const char* ssid = "";
const char* password = "";

const char* accountkey = "";
const char* apiurl = "https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival?BusStopCode=66271";
const char* busstopcode = "66271";

struct tm tm;
char readabletime[16];

char timings[8][3][8];



int arrivalinminutes = 0;

StaticJsonDocument<8192> doc;

                           
const char busstoptext[] = "Bus Stop 66271 Arrivals";
const int busstoptexty = 2;
const int busstoptextx = 20;
const int busstoptextplus = 2;
const int spacebetweenbustimingsy = 52; //keep even
const int important2x = 510;

const int busarrivalsx = 300;
const int spacebetweenarrival = 75;
const char* servicestringlist[] = {
  "136 > PUNGGOL INT.",
  "136 > AMK INT.",
  "315 > S'GOON INT.",
  "315 > NORTH AVE.",
  "317 > S'GOON INT.",
  "317 > BERWICK DR.",
  "73 > AMK INT.", 
  "73 > TOA PAYOH"
};

void timeReadable(){
  struct tm timeinfo;

  if (getLocalTime(&timeinfo)) {
  strftime(readabletime, sizeof(readabletime), "%I:%M:%S %p", &timeinfo);
  }
  else{
    strcpy(readabletime, "ERRORERRORERROR");
  };
  Serial.println(readabletime);
  return;
};

void debugPrintTimings(){
  for (int i = 0; i < 8; i++){
    Serial.print("\nindex ");
    Serial.print(i);

    Serial.print(", buses: ");
    for (int j = 0; j < 3; j++){
      Serial.print(j);
      Serial.print(" : ");
      Serial.print(timings[i][j]);
      Serial.print("|");
    }
  }
}

void syncTime() {
    Serial.println("syncTime called");

    configTime(8 * 3600, 0, "pool.ntp.org", "time.nist.gov"); // UTC+8
    time_t now = time(NULL);

    Serial.print("Waiting for time");
    while (now < 1600000000) { // time not valid yet
        delay(500);
        Serial.print(".");
        now = time(NULL);
    }
    Serial.println("\nTime synced.");
}



void insertTime(const char* timestamp, int timingsserviceindex, int timingsbusindex) {
  Serial.println("insertTime called");
  if (strcmp(timestamp, "") == 0) {
    Serial.println("insertTime returned, timing: None");
    return;
  }
  time_t arrivalepoch;
  struct tm tm;
  if (strptime(timestamp, "%Y-%m-%dT%H:%M:%S", &tm)) {
        arrivalepoch = mktime(&tm);
  }
  else {
    Serial.println("ERROR IN insertTime: STRPTIME");
  }
  
  
  time_t now = time(NULL);
  arrivalinminutes = (arrivalepoch - now)/60.0;  //rounded down
  Serial.println("insertTime returned, timing: ");
  Serial.println(arrivalinminutes);
  Serial.println(timestamp);

  snprintf(timings[timingsserviceindex][timingsbusindex], sizeof(timings[timingsserviceindex][timingsbusindex]), "%d", arrivalinminutes);

  return;
};


void nextbusesfunction(JsonObject service, const char* busnum){
  int dictindex = -1;
  for (int i = 0; i < (sizeof(dict) / sizeof(dict[0])); i++) {
    if (strcmp(dict[i].servicenum, busnum) == 0) {
      dictindex = i;
      break;
    }
  }
  for (const char* nextbus : nextbusarray) {
    const char* visitnumber = service[nextbus]["VisitNumber"];
    const char* timestamp = service[nextbus]["EstimatedArrival"];
    if (strncmp(visitnumber, "2", 1) == 0) {
      insertTime(timestamp, dict[dictindex].direction2, dict[dictindex].direction2count);
      dict[dictindex].direction2count = dict[dictindex].direction2count + 1;
    }
    else {
      insertTime(timestamp, dict[dictindex].direction1, dict[dictindex].direction1count);
      dict[dictindex].direction1count = dict[dictindex].direction1count + 1;
    }
  }
}


void parseJson() {
  //136 to punggol

  for (int i = 0; i < 3; i++) {
    dict[i].direction1count = 0;
    dict[i].direction2count = 0;
  }
  struct1 dict[] = {
  {"315", 5, 4, 0, 0},
  {"317", 3, 2, 0, 0},
  {"73", 7, 6, 0, 0}
  };
  Serial.println("/nparseJson called");
  JsonArray services = doc["Services"].as<JsonArray>();

  for (JsonObject service : services) {
    const char* servicenum = service["ServiceNo"];
    const char* origincode = service["NextBus"]["OriginCode"];
    Serial.println("\nLOOP: servicenum: ");
    Serial.println(servicenum);
    Serial.println(" , origincode: ");
    Serial.println(origincode);
    if (strcmp(servicenum, "136") == 0 && strcmp(origincode, "54009") == 0) { //136 to punggol int
      Serial.println("\nFound 136 to punggol, calling insertime with nextbus times");
      const char* nextbustime = service["NextBus"]["EstimatedArrival"];
      const char* nextbus2time = service["NextBus2"]["EstimatedArrival"];
      const char* nextbus3time = service["NextBus3"]["EstimatedArrival"];
      const char* visitnumber = service["NextBus"]["VisitNumber"];
      insertTime(nextbustime, 0, 0);
      insertTime(nextbus2time, 0, 1);
      insertTime(nextbus3time, 0, 2);
    }
    else if (strcmp(servicenum, "136") == 0 && strcmp(origincode, "65009") == 0) { //136 to amk int
      Serial.println("\nFound 136 to amk, calling insertime with nextbus times");
      const char* nextbustime = service["NextBus"]["EstimatedArrival"];
      const char* nextbus2time = service["NextBus2"]["EstimatedArrival"];
      const char* nextbus3time = service["NextBus3"]["EstimatedArrival"];
      insertTime(nextbustime, 1, 0);
      insertTime(nextbus2time, 1, 1);
      insertTime(nextbus3time, 1, 2);
    }
    else if (strcmp(servicenum, "73T") == 0) { //ignore 73T
      ;
    }
    else {
      nextbusesfunction(service, servicenum);
    }
  }
};




void connectWifi(){
  client.setCACert(rootca);
  WiFi.begin(ssid, password);
  int count = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    count++;
    if (count > 15){
      Serial.print("RESTART");
      connectWifi();
    }
  }

  Serial.println("\nConnected to Wi-Fi");
  return;
};



void getBusTimings() {

  memset(timings, 0, sizeof(timings));

  if (WiFi.status() != WL_CONNECTED){
    Serial.println("\nNot connected, trying to connect");
    connectWifi();
  }

  HTTPClient http;                 
  http.begin(client, apiurl);              
  http.addHeader("AccountKey", accountkey);   

  int httpresponsecode = http.GET();

  Serial.println("\nHttp response code:");
  Serial.println(httpresponsecode);


  if (httpresponsecode > 0) {
    String payload = http.getString(); // Read response as a String
    Serial.println("\nRecieved:");
    Serial.println(payload);
    DeserializationError error = deserializeJson(doc, payload);
    if (error) {
        Serial.print("JSON parse failed: ");
        Serial.println(error.c_str());
        return;
    }
    parseJson();
  }
  else{
    Serial.println("\nError in http request:");
    Serial.println(httpresponsecode);

  }

};


void printToDisplay()
{
  display.setRotation(0);
  display.setFont(&FreeMonoBold18pt7b);
  display.setTextSize(1);
  display.setTextColor(GxEPD_WHITE);
  int16_t tbx, tby; uint16_t tbw, tbh;
  display.getTextBounds(busstoptext, 0, 0, &tbx, &tby, &tbw, &tbh);
  // center the bounding box by transposition of the origin:
  uint16_t x = busstoptextx - tbx;
  uint16_t y = busstoptexty - tby;
  display.setFullWindow();
  display.firstPage();

  do
  {
    display.fillScreen(GxEPD_WHITE);
    display.setCursor(x, y);
    display.fillRect(busstoptextx - busstoptextplus, busstoptexty - busstoptextplus, tbw + busstoptextplus*2, tbh + busstoptextplus*2, GxEPD_BLACK);
    display.setTextColor(GxEPD_WHITE);
    display.print(busstoptext);

    display.setFont(&FreeMonoBold12pt7b);
    display.setTextColor(GxEPD_BLACK);
    y += spacebetweenbustimingsy/2;
    display.fillRect(busstoptextx - busstoptextplus, y, tbw + busstoptextplus*2, 2, GxEPD_BLACK);
    y += spacebetweenbustimingsy/2;
    int16_t tbx2, tby2; uint16_t tbw2, textheight;
    for (int i = 0; i < sizeof(servicestringlist)/sizeof(servicestringlist[0]); i++) {
      display.getTextBounds(servicestringlist[i], 0, 0, &tbx2, &tby2, &tbw2, &textheight);
      display.setCursor(x, y+textheight/2);
  
      display.setFont(&FreeMonoBold12pt7b);
      display.print(servicestringlist[i]);


      display.setFont(&FreeMonoBold18pt7b);

      for (int j = 0; j < 3; j++) {
        display.getTextBounds(timings[i][j], 0, 0, &tbx2, &tby2, &tbw2, &textheight);
        display.setCursor(busarrivalsx + spacebetweenarrival*j, y+textheight/2);
        display.print(timings[i][j]);
      }

      y += spacebetweenbustimingsy/2;
      display.fillRect(busstoptextx - busstoptextplus, y, tbw + busstoptextplus*2, 2, GxEPD_BLACK);
      y += spacebetweenbustimingsy/2;
    };
    for (int i = 0; i < 2; i++) {
      display.setFont(&FreeMonoBold9pt7b);
      display.setTextSize(1);
      display.getTextBounds(important2[i], 0, 0, &tbx2, &tby2, &tbw2, &textheight);
      display.setCursor(important2x, 0+240*i+textheight);
      display.print(important2[i]);


      uint16_t tbh2;
      display.setFont(&FreeMonoBold24pt7b);
      display.setTextSize(5);
      display.getTextBounds(timings[2*i+2][0], 0, 0, &tbx2, &tby2, &tbw2, &tbh2);
      display.setCursor(busstoptextx + tbw, 0+240*i+textheight+20+ tbh2);
      display.print(timings[2*i+2][0]);
      if (strlen(timings[2*i+2][0])<2 && strcmp(timings[2*i+2][1], "") != 0 ){
        Serial.println("Able to fit 2 timings");
        int16_t tbx3, tby3; uint16_t tbw3, tbh3;
        display.setTextSize(3);
        display.getTextBounds(timings[2*i+2][1], 0, 0, &tbx3, &tby3, &tbw3, &tbh3);

        display.fillRect(busstoptextx+5 + tbw + tbw2+30, textheight+5 +240*i, 2 , 180, GxEPD_BLACK);
        display.setCursor(busstoptextx + tbw + tbw2+36, 0+240*i+textheight+20+ tbh3);
        display.print(timings[2*i+2][1]);
      
      }
    }
    display.setFont(&FreeMonoBold18pt7b);
    display.setTextSize(1);
    display.setCursor(busstoptextx + tbw,476);
    timeReadable();
    display.print(readabletime);
  }
  while (display.nextPage());
};




void setup()
{
  Serial.begin(115200);
  delay(1500);
  display.init(115200, true, 2, false);
  Serial.println("NEWEWnEWNEWNEWNEW");

  display.setFullWindow();
  display.firstPage();
  do {
    display.fillScreen(GxEPD_WHITE);
  } while (display.nextPage());

  delay(500);


  Serial.println("\nNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEWNEW");
  connectWifi();
  syncTime();
  getBusTimings();
  debugPrintTimings();
  printToDisplay();
  
}

void loop() {
  delay(20000);
  Serial.println("\Delay finished, refreshing page");
  connectWifi();
  getBusTimings();
  debugPrintTimings();
  printToDisplay();
};
