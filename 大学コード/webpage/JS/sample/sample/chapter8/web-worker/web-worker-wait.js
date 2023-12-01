	// 送信されたデータを取得
	onmessage = function(event) {
		// データをコンソールに出力
		console.log('@worker', event.data);

		// 時間のかかる処理
		for (let i = 0; i < 5000; i ++) {
			const str = [...'@'.repeat(5000)].join();

			// 1000ごとにコンソールに経過を出力
			if (i % 1000 === 0) {
				console.log('@worker', i);
			}
		}

		// 呼び出し元にデータを送信
		postMessage('返信！');
	};