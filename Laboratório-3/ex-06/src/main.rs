// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

static HOST: &str = "127.0.0.1";
static PORT: i32 = 56906;
static DB_PORT: i32 = 56907;

fn handle_connection(mut client_stream: TcpStream) {
    let mut buffer1 = [0; 1024];
    let mut buffer2 = [0; 1024];
    let n = client_stream.read(&mut buffer1).unwrap();

    let client_data = str::from_utf8(&buffer1[..n]).unwrap();
    
    let mut stream = TcpStream::connect(format!("{}:{}", HOST, DB_PORT)).unwrap();
    stream.write(client_data.as_bytes()).unwrap();

    let n = stream.read(&mut buffer2).unwrap();
    let data = str::from_utf8(&buffer2[..n]).unwrap().split(',').collect::<Vec<&str>>();
    
    let nome = client_data;
    let nivel = data[0];
    let salario = data[1].parse::<f32>().unwrap();
    let dependentes = data[2].parse::<i8>().unwrap();
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

    client_stream.write(response.as_bytes()).unwrap();
    client_stream.flush().unwrap();
}

fn main() {
    let addr: String = format!("{}:{}", HOST, PORT);
    let listener = TcpListener::bind(addr).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        
        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}