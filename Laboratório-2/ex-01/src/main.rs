// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer).unwrap();

    let data = str::from_utf8(&buffer[..n]).unwrap().split(',').collect::<Vec<&str>>();
    let nome = data[0];
    let cargo = data[1];
    let mut salario = data[2].parse::<f32>().unwrap();

    if cargo == "operador" {
        salario *= 1.2;
    } else if cargo == "programador" {
        salario *= 1.18;
    }

    let response = format!("O funcionário {} tem como novo salário R${:.2}", nome, salario);

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}

fn main() {
    let host = "127.0.0.1";
    let port = 56895;
    let addr: String = format!("{}:{}", host, port);
    let listener = TcpListener::bind(addr).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        
        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}