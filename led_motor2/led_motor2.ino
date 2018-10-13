const int ledRojo =2;
const int BOTON = 7;
const int motor = 13;
const int BOTON2 = 4;
const int pinbtn = 3;
int led1=10,led2=11,pulse=5;
int val = 0; 
int state = 0; 
int old_val = 0; 
void setup(){
 pinMode(ledRojo,OUTPUT); 
 pinMode(BOTON,INPUT);
 pinMode(motor,OUTPUT); 
 pinMode(BOTON2,INPUT);
 pinMode(pulse,INPUT);
}
int x=0;
void loop() {      
val= digitalRead(BOTON); 
if ((val == HIGH) && (old_val == LOW)){
state=1-state;
delay(10);
}
old_val = val; 
if (state==1){
 digitalWrite(ledRojo, HIGH); 
}
else{
 digitalWrite(ledRojo,LOW); 
}
{      
val= digitalRead(BOTON2); 
if ((val == HIGH) && (old_val == LOW)){
state=1-state;
delay(10);
}
old_val = val; 
if (state==1){
 digitalWrite(motor, HIGH); 
}
else{
 digitalWrite(motor,LOW); 
}
}
switch(x) 
{
case 1:
if (digitalRead(pulse) == HIGH){digitalWrite(led1,HIGH);} else {digitalWrite(led1,LOW);}
break;
case 2:
if (digitalRead(pulse) == HIGH){digitalWrite(led2,HIGH);} else {digitalWrite(led2,LOW);}
break;
{
}
}
}
