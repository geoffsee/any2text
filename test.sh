HOST=https://any2text.seemueller.io
#HOST=https://flaskproject-nameless-feather-9941.fly.dev
#HOST=http://localhost:5006

curl -X POST -F "file=@sample.pdf" "${HOST}/extract"
