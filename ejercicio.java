/******************************************************************************

 temp=float(input("temperatura registrada"))
if temp>=27: print("pongase algo fresco")
elif temp>-20 and temp<27: print("abrigate")
elif temp>16 and temp<20: print("abrigate mas")
else: print("esta helando")
*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    
		System.out.println("temperatura registrada:");
		Scanner leer= new Scanner(System.in);
		//nextLine es para String
		//nextLine es para leer decimales
		
		
		float temp = leer.nextFloat();
		//&& and || on 
		if (temp>=27){System.out.println("pongase algo fresco");}
		else if(temp>=20 &&temp<=27){System.out.println("abrigate");}
		else if (temp>=16 && temp<20){System.out.println("abrigate más");}
		else {System.out.println("esta helado");}
		
		//ejercicio para easy hand
		System.out.println("cual es tu edad?");
		int edad = leer.nextInt();
		System.out.println(edad>=18? "eres mayor de edad":"no eres mayor de edad");
	}
}