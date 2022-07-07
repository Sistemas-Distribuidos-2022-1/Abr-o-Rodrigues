// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer).unwrap();

    let data = str::from_utf8(&buffer[..n]).unwrap().split(',').collect::<Vec<&str>>();
    println!("{:?}", data);
    let nome = data[0];
    let sexo = data[1];
    let idade = data[2].parse::<i8>().unwrap();
    let resultado: &str;

    if sexo == "masculino" && idade >= 18 {
        resultado = "atingiu a maioridade.";
    } else if sexo == "feminino" && idade >= 21 {
        resultado = "atingiu a maioridade.";
    } else {
        resultado = "não atingiu a maioridade.";
    }

    let response = format!("{} {}", nome, resultado);

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}

fn main() {
    let host = "127.0.0.1";
    let port = 56898;
    let addr: String = format!("{}:{}", host, port);
    let listener = TcpListener::bind(addr).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        
        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}