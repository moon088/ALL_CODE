	// 送信されたデータを取得
	onmessage = function(event) {
		// データをJSON化して、コンソールに出力
		console.log('@worker', JSON.stringify(event.data));

		// 返信するデータを作成
		const data = {msg: '返信！', arr: [4, 5, 6]};

		// 呼び出し元にデータを送信
		postMessage(data);
	};