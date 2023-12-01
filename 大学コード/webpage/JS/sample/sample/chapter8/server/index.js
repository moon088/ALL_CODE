	const express = require('express');
	const app = express();

	// ルート
	app.get('/', (req, res) => {
		res.send('Hello World');
	});

	// 設定の配列
	const optArr = [
		{path: '/net', root: __dirname + '/../net'},
		{path: '/web-worker', root: __dirname + '/../web-worker'}
	];

	// 各設定の、静的ファイル読み込み受付を開始する
	optArr.forEach(x => {
		console.log(x.path, x.root);
		app.use(x.path, express.static(x.root));
	});

	// 受付開始（http://localhost:3000/...）
	app.listen(3000);