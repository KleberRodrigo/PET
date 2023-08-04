#include <stdio.h>
#include <webots/robot.h>
#include <webots/motor.h>
#include <webots/position_sensor.h>
#include <math.h>
#include <time.h>
#include <webots/keyboard.h>
#include <webots/robot.h>

#define TIME_STEP 64

int main(int argc, char **argv) 
{

   wb_robot_init();
   wb_keyboard_enable(TIME_STEP);

   //Declaração de Variaveis  
   int i=0;
   int key=-1;
   float posicao[10][7];
   float posicao_atual[7];
   float step_arm = 0.001;
   int motor = 0;
   //Motor =             -1-  -2-  -3-  -4-   -5-  -6-
   float vel[7] = {0.0, 1, 1, 1, 1, 3, 1};
   
   //Definição de Motores
   WbDeviceTag M[7];
   M[1] = wb_robot_get_device("motor1");
   M[2] = wb_robot_get_device("motor2");
   M[3] = wb_robot_get_device("motor3");
   M[4] = wb_robot_get_device("motor4");
   M[5] = wb_robot_get_device("motor5");
   M[6] = wb_robot_get_device("motor6");
   
   //Definição de Sensor de Posição
   WbDeviceTag s_position[7];
    s_position[1] = wb_robot_get_device("position1");
    s_position[2] = wb_robot_get_device("position2");
    s_position[3] = wb_robot_get_device("position3");
    s_position[4] = wb_robot_get_device("position4");
    s_position[5] = wb_robot_get_device("position5");
    s_position[6] = wb_robot_get_device("position6");
    
    for(i=1;i<7;i++)
     wb_position_sensor_enable(s_position[i], TIME_STEP);
   
   //Definição de Velocidade de cada motor
   for(i=1;i<7;i++)
     wb_motor_set_velocity(M[i], vel[i]);
   
   //Definição da Posição de trabalho do Robo
   posicao[0][1] = 0.0;
   posicao[0][2] = 0.72;
   posicao[0][3] = 0.51;
   posicao[0][4] = 0.0;
   posicao[0][5] = -1.24;
   posicao[0][6] = 0.0;
   
   //Definição da Posição de Home do Robo
   posicao[1][1] = 0.0;
   posicao[1][2] = 0.0;
   posicao[1][3] = 0.0;
   posicao[1][4] = 0.0;
   posicao[1][5] = 0.0;
   posicao[1][6] = 0.0;
   
   //Loop
  while (wb_robot_step(TIME_STEP) != -1) 
  {
  
    float HOME[6] = {0, 0, -1.5708, 0, 0, 0};
    
    for(i=0; i<6; i++)
    {
      wb_motor_set_position(M[i+1], HOME[i]);
    }
  
  /*
   key = wb_keyboard_get_key();
     
   if (key >= 0)
   {  
      printf("\n ---------------------------------"); 
      printf("\n Key: %d",key);
      
      switch (key) 
      {
        case '1':
          motor = 1; 
        break;
          
        case '2':
          motor = 2;
        break;
          
        case '3':
          motor = 3;
        break;
          
        case '4':
          motor = 4;
        break;
          
        case '5':
          motor = 5;
        break;
          
        case '6':
          motor = 6;
        break;
          
        case 73: //Posição inicial - Tecla : "I"
          for(i=1;i<7;i++)
              wb_motor_set_position(M[i],  posicao[0][i]);
        break;
        
        case 72: //Posição inicial - Tecla : "H"
          for(i=1;i<7;i++)
              wb_motor_set_position(M[i],  posicao[1][i]);
        break;
          
        case WB_KEYBOARD_UP: //Movimentar robo
          if(motor > 0)
          {
            posicao_atual[motor] = (round(wb_position_sensor_get_value(s_position[motor])*1000))/1000;
            posicao_atual[motor] = posicao_atual[motor] + step_arm;
            wb_motor_set_position(M[motor],posicao_atual[motor]);
            printf("\n Motor %d , Posicao Para atual: %.3f",motor,posicao_atual[motor]);
          }
        break;
          
        case WB_KEYBOARD_DOWN: //Movimentar robo
          if(motor > 0)
          {
            posicao_atual[motor] = wb_position_sensor_get_value(s_position[motor]);
            posicao_atual[motor] = posicao_atual[motor] - step_arm;
            wb_motor_set_position(M[motor],posicao_atual[motor]);
            printf("\nMotor %d , Posicao %.3f\n",motor,posicao_atual[motor]);
          }
        break;
          
        case 85: //Velocidade de step alta - Tecla U
          step_arm = 0.01;
        break;
          
        case 76: //Velocidade de step baixa - Tecla l
          step_arm = 0.001;
        break;
          
        case 65: //Automático - Tecla A
        break;
         
        case 80://Imprimir posição atual do Robô - Tecla P
          for(i=1;i<7;i++)
            posicao_atual[i]= round(wb_position_sensor_get_value(s_position[i])*1000)/1000;
          printf("\nPos=  {%.3f,%.3f,%.3f,%.3f,%.3f,%.3f}, \n",posicao_atual[1],posicao_atual[2],posicao_atual[3],posicao_atual[4],posicao_atual[5],posicao_atual[6]);   
        break;  
       }
    
     while(key!=-1)
        {
          wb_robot_step(10);
          key = wb_keyboard_get_key();
        }
    }*/
};
  
  
wb_robot_cleanup();

  return 0;
}
