package main

import (
	"github.com/tivvit/shus/go-shus/backend"
	"net/http"
)

var b backend.Backend

func main() {
	b = backend.NewJsonFile("urls.json")

	http.HandleFunc("/", ShortHandler)
	http.ListenAndServe(":80", nil)
}

func ShortHandler(w http.ResponseWriter, r *http.Request) {
	short := r.URL.Path[1:]
	url, err := b.Get(short)
	if err != nil {
		w.WriteHeader(http.StatusNotFound)
	} else {
		http.Redirect(w, r, url, http.StatusFound)
	}
}
