	// カウンター用変数
	let cnt = 0;

	// 送信されたデータを取得
	onconnect = function(event) {
		const port = event.ports[0];

		port.onmessage = function(event) {
			// データをコンソールに出力
			console.log('@worker', event.data);

			// 呼び出し元にデータを送信
			port.postMessage(`返信！${++ cnt}`);
		};
	};