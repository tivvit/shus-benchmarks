#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use]
extern crate rocket;

use std::fs;
use lazy_static::lazy_static;
use rocket::response::Redirect;
use std::collections::HashMap;
use std::io::Read;
use std::time::Instant;

lazy_static! {
    static ref KNOWN_URLS: HashMap<String, String> = {
        let mut file = fs::File::open("urls.json").expect("file should open (read only)");
        println!("File loaded");
        let now = Instant::now();
        let mut data_str: String = String::from("");
        file.read_to_string(&mut data_str).expect("file should load");
        let known_urls: HashMap<String, String> = serde_json::from_str(&data_str).expect("json is not valid");
        println!("JSON loaded in {} ms", now.elapsed().as_millis());
        known_urls
    };
}

#[get("/<short>")]
fn short(short: &str) -> Option<Redirect> {
    match KNOWN_URLS.get(short) {
        None => None,
        Some(target) => Some(rocket::response::Redirect::found(target))
    }
}

#[launch]
fn rocket() -> _ {
    // Preload data
    KNOWN_URLS.is_empty();
    rocket::build().mount("/", routes![short])
}