/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package holamundo;
import java.util.Scanner; //PARA IMPORTAR LA LIBRERIA DEL TECLADO


/**
 *
 * @author zharick parada 
 */
public class Holamundo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // esto es un comenrario, vamos a saludar a el mundo 
        System.out.println("hola mundo, distrito PROGCOM");
        
        Scanner leer= new Scanner(System.in);
        System.out.println("esta lloviendo?");
        



//creando un objeto que recibira la respuesta 
        String respuesta= leer.nextLine();
     
        System.out.println("tu respuesta fue: " + respuesta);   
        //programamando con if/else
        if (respuesta=="no"){
            System.out.println("te recomueno ir a el parque");
        }
    }
    
}
