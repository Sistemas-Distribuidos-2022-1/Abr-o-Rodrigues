// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer).unwrap();

    let data = str::from_utf8(&buffer[..n]).unwrap().split(',').map(|x| x.parse::<f32>().unwrap()).collect::<Vec<f32>>();
    let n1 = data[0];
    let n2 = data[1];
    let n3 = data[2];

    let m = (n1 + n2) / 2.0;
    let resultado: &str;

    if m >= 7.0 {
        resultado = "Aprovado";
    } else if m >= 3.0 && (m + n3) / 2.0 >= 5.0 {
        resultado = "Aprovado";
    } else {
        resultado = "Reprovado";
    }

    let response = resultado;

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}

fn main() {
    let host = "127.0.0.1";
    let port = 56900;
    let addr: String = format!("{}:{}", host, port);
    let listener = TcpListener::bind(addr).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        
        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}