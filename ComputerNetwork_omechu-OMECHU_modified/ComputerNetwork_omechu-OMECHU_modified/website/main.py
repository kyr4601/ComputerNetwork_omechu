from init import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='localhost', port=2023, debug=True)
    # debug 모드에서는 파일 수정 시 수정사항 바로 반영됨


