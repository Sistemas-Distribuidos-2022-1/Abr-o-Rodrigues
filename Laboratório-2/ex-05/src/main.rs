// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer).unwrap();

    let data = str::from_utf8(&buffer[..n]).unwrap();
    let idade = data.parse::<i8>().unwrap();
    let resultado: &str;

    if idade >= 18 {
        resultado = "adulto";
    } else if idade >= 14 {
        resultado = "juvenil B";
    } else if idade >= 11 {
        resultado = "juvenil A";
    } else if idade >= 8 {
        resultado = "infantil B";
    } else if idade >= 5 {
        resultado = "infantil A";
    } else {
        resultado = "nenhuma";
    }

    let response = format!("Categoria {}", resultado);

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}

fn main() {
    let host = "127.0.0.1";
    let port = 56902;
    let addr: String = format!("{}:{}", host, port);
    let listener = TcpListener::bind(addr).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        
        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}