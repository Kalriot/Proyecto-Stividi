/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.mavenproject3;
import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 *
 * @author Tutur
 */
public class Mavenproject3 {

    public static void main(String[] args) {
         try {
            // Comando para ejecutar el script Python
            ProcessBuilder processBuilder = new ProcessBuilder("python", "script.py");

            // Iniciar el proceso
            Process process = processBuilder.start();

            // Leer la salida estándar
            BufferedReader stdOutput = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            System.out.println("Salida del script Python:");
            while ((line = stdOutput.readLine()) != null) {
                System.out.println(line);
            }

            // Leer la salida de error
            BufferedReader errorOutput = new BufferedReader(new InputStreamReader(process.getErrorStream()));
            System.out.println("Errores del script Python:");
            while ((line = errorOutput.readLine()) != null) {
                System.out.println(line);
            }

            // Esperar a que el proceso termine
            int exitCode = process.waitFor();
            System.out.println("Script Python ejecutado con código de salida: " + exitCode);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
