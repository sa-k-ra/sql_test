# vulnerable_app/views.py
from django.http import HttpResponse
from django.db import connection
import sqlite3
from django.shortcuts import render

def search_user(request):
    username = request.GET.get('username', None)
    
    if username:
        # SQLインジェクションの脆弱性を含んだクエリ
        query = f"SELECT * FROM vulnerable_app_user WHERE username = '{username}'"
        
        # データベース接続
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.execute(query)
        
        # 結果を取得
        user = cursor.fetchone()
        
        connection.close()
        
        if user:
            return render(request, 'search_result.html', {'user': user})
        else:
            return render(request, 'search_result.html', {'message': 'User not found'})
    
    return render(request, 'search_result.html', {'message': 'No username provided'})
