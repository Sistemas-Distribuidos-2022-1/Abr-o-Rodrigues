// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

static HOST: &str = "127.0.0.1";
static PORT: i32 = 56904;
static DB_PORT: i32 = 56905;

fn handle_connection(mut client_stream: TcpStream) {
    let mut buffer1 = [0; 1024];
    let mut buffer2 = [0; 1024];
    let n = client_stream.read(&mut buffer1).unwrap();

    let client_data = str::from_utf8(&buffer1[..n]).unwrap();
    
    let mut stream = TcpStream::connect(format!("{}:{}", HOST, DB_PORT)).unwrap();
    stream.write(client_data.as_bytes()).unwrap();

    let n = stream.read(&mut buffer2).unwrap();
    let data = str::from_utf8(&buffer2[..n]).unwrap();
    
    let nome = client_data;
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

    let response = format!("{} está na categoria {}", nome, resultado);

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