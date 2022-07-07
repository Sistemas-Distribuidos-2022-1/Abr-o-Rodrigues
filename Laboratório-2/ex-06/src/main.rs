// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer).unwrap();

    let data = str::from_utf8(&buffer[..n]).unwrap().split(',').collect::<Vec<&str>>();
    let nome = data[0];
    let nivel = data[1];
    let salario = data[2].parse::<f32>().unwrap();
    let dependentes = data[3].parse::<i8>().unwrap();
    let mut resultado: f32 = 0.0;

    if nivel == "A" {
        if dependentes == 0 {
            resultado = salario * 0.97;
        } else {
            resultado = salario * 0.92;
        }
    } else if nivel == "B" {
        if dependentes == 0 {
            resultado = salario * 0.95;
        } else {
            resultado = salario * 0.90;
        }
    } else if nivel == "C" {
        if dependentes == 0 {
            resultado = salario * 0.92;
        } else {
            resultado = salario * 0.85;
        }
    } else if nivel == "D" {
        if dependentes == 0 {
            resultado = salario * 0.90;
        } else {
            resultado = salario * 0.83;
        }
    } 

    let response = format!("Funcionário {} de nivel {} tem como salário liquido R${:.2}", nome, nivel, resultado);

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}

fn main() {
    let host = "127.0.0.1";
    let port = 56903;
    let addr: String = format!("{}:{}", host, port);
    let listener = TcpListener::bind(addr).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        
        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}