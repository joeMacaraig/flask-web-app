from website import create_app #importing package

app = create_app()

if __name__ == '__main__': 
    app.run(debug=True)

