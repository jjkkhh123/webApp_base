from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# 홈 페이지 라우트
@app.route('/')
def index():
    return render_template('index.html')

# 폼 제출을 처리하는 라우트
@app.route('/add', methods=['POST'])
def add_contact():
    이름 = request.form['pyname']
    전화번호 = request.form['pyphone']
    생일 = request.form['pybirth']

    # addbook.txt 파일에 CSV 형식으로 저장
    with open('addbook.txt', 'a', newline='', encoding='utf-8') as 파일:
        작성자 = csv.writer(파일)
        작성자.writerow([이름, 전화번호,생일])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)