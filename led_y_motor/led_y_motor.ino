char opcion = "0";
int ledRojo = 2;
int motor = 13;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
   pinMode(2,OUTPUT);
   pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0)
 { 
  opcion = Serial.read();
 }
   if(opcion=="0")
   {
    Serial.println("menu");
    Serial.println("1.Encender led Rojo");
    Serial.println("2.Apagar led Rojo"); 
    Serial.println("3.Encender motor"); 
    Serial.println("4.Apagar motor");
    Serial.println("5.Encender led Rojo y motor");
    Serial.println("6.Apagar led Rojo y motor");
   }
    if(opcion=="1")
   {
    digitalWrite(2,HIGH);
   }else{
    if(opcion=="2")
    {
      digitalWrite(2,LOW);
    }else{
      Serial.println("opcionIncorrecta");
    }
    
    
    if(opcion=="3")
   {
    digitalWrite(13,HIGH);
   }else{
    if(opcion=="4")
    {
      digitalWrite(13,LOW);
    }else{
      Serial.println("opcionIncorrecta");
    }
     
     
     if(opcion=="5")
   {
    digitalWrite(2,HIGH);
    digitalWrite(13,HIGH);
   }else{
    if(opcion=="6")
    {
      digitalWrite(2,LOW);
      digitalWrite(13,LOW);
    }else{
      Serial.println("opcionIncorrecta");
    }


    
   }
    
   }
   }
} 
   
