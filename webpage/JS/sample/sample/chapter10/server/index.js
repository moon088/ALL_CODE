	// 設定
	const dirImages = 'upload_images/';  // 投稿画像を保存するフォルダ
	const filePostDat = 'post-dat.txt';  // 投稿コメントを保存するファイル

	// モジュールの読み込み
	const fs = require('fs');
	const express = require('express');
	const app = express();
	const multer = require('multer');
	const upload = multer({dest: dirImages})

	// ルート
	app.get('/', (req, res) => {
		res.send('Hello World');
	});

	// 静的ページの表示
	app.use('/app', express.static(__dirname + '/../app'));
	app.use('/upload_images', express.static(__dirname + '/upload_images'));

	// 投稿の受付
	app.post('/post', upload.any(), (req, res) => {
		// 受け取った情報をコンソールに表示
		console.log(req.body);
		console.log(req.files);

		// 情報を作成
		const objSave = {
			comment: req.body.comment,
			dir: dirImages,
			image: req.files[0].filename,
			date: Date.now()
		};
		const txtSave = JSON.stringify(objSave) + '\n';
		console.log(txtSave);

		// 情報を保存
		fs.appendFile(filePostDat, txtSave, err => {
			console.log(err);
		});

		// レスポンス
		const resObj = {
			message: 'Received POST Data!',
			status: 'success'
		};
		res.send(JSON.stringify(resObj));
	});

	// 投稿データの取得
	app.get('/get', (req, res) => {
		// 情報を読み込み
		fs.readFile(filePostDat, 'utf8', (err, data) => {
			// 事前処理
			data = data.trim().replace(/\r/g, '');
			const arr = data.split('\n');
			arr.reverse();

			// 文字列の作成
			const txt = '{"list": [' + arr.join(',') + ']}';

			// 返信
			res.type('json');
			res.send(txt);
		});
	});

	// 受付開始（http://localhost:3000/...）
	const port = 3000;
	app.listen(3000, () => console.log('start server.'));