// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer).unwrap();

    let data = str::from_utf8(&buffer[..n]).unwrap().split(',').map(|x| x.parse::<i8>().unwrap()).collect::<Vec<i8>>();
    let idade = data[0];
    let tempo = data[1];
    let resultado: &str;

   if idade >= 65 && tempo >= 30 {
    resultado = "Pode se aposentar";
   } else if idade >= 60 && tempo >= 25 {
    resultado = "Pode se aposentar";
   } else {
    resultado = "Não pode se aposentar";
   }

    let response = resultado;

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}

fn main() {
    let host = "127.0.0.1";
    let port = 56904;
    let addr: String = format!("{}:{}", host, port);
    let listener = TcpListener::bind(addr).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();
        
        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}