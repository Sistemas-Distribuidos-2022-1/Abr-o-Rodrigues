// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer).unwrap();

    let data = str::from_utf8(&buffer[..n]).unwrap().split(',').collect::<Vec<&str>>();
    let altura = data[0].parse::<f32>().unwrap();
    let sexo = data[1];
    let resultado: f32;

    if sexo == "masculino" {
        resultado = 72.7 * altura - 58.0;
    } else {
        resultado = 62.1 * altura - 44.7;
    }

    let response = format!("O peso ideal é de {:.2}kgs", resultado);

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}

fn main() {
    let host = "127.0.0.1";
    let port = 56901;
    let addr: String = format!("{}:{}", host, port);
    let listener = TcpListener::bind(addr).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        
        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}