// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer).unwrap();

    let data = str::from_utf8(&buffer[..n]).unwrap();
    let saldo_medio = data.parse::<f32>().unwrap();
    let resultado: f32;

    if saldo_medio >= 601.0 {
        resultado = saldo_medio * 0.4;
    } else if saldo_medio >= 401.0 {
        resultado = saldo_medio * 0.3;
    } else if saldo_medio >= 201.0 {
        resultado = saldo_medio * 0.2;
    } else  {
        resultado = 0.0;
    }

    let response = format!("Com o saldo médio de R${:.2} tem-se R${:.2} de crédito", saldo_medio, resultado);

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}

fn main() {
    let host = "127.0.0.1";
    let port = 56905;
    let addr: String = format!("{}:{}", host, port);
    let listener = TcpListener::bind(addr).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        
        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}