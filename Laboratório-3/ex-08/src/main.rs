// O código compilado está em target/debug/nome_da_pasta.exe

use std::{net::{TcpListener, TcpStream}, thread};
use std::io::prelude::*;
use std::str;

static HOST: &str = "127.0.0.1";
static PORT: i32 = 56910;
static DB_PORT: i32 = 56911;

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

    let response = format!("{} com o saldo médio de R${:.2} tem R${:.2} de crédito", nome, saldo_medio, resultado);

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