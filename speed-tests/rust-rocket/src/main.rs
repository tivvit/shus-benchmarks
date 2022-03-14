#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use]
extern crate rocket;

use std::fs;
use lazy_static::lazy_static;
use rocket::response::Redirect;
use std::collections::HashMap;

lazy_static! {
    static ref KNOWN_URLS: HashMap<String, String> = {
        let file = fs::File::open("urls.json").expect("file should open (read only)");
        println!("File loaded");
        let known_urls: HashMap<String, String> = serde_json::from_reader(file)
        .expect("file should be proper JSON");
        println!("JSON loaded");
        known_urls
    };
}

#[get("/<short>")]
fn short(short: &str) -> Option<Redirect> {
    match KNOWN_URLS.get(short) {
        None => None,
        Some(target) => Some(rocket::response::Redirect::found(String::from(target)))
    }
}

#[launch]
fn rocket() -> _ {
    // Preload data
    KNOWN_URLS.is_empty();
    rocket::build().mount("/", routes![short])
}