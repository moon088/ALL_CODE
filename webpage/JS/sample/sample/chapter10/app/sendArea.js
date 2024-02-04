	// windowにDOMContentLoadedの処理を登録
	window.addEventListener('DOMContentLoaded', e => {
		// 要素
		const elSend = document.querySelector('#send');
		const elCmnt = document.querySelector('#comment');

		// Canvas関係の要素
		const canvas = document.querySelector('#view');

		//--------------------
		// 投稿ボタン クリックの処理
		elSend.addEventListener('click', e => {
			// データ送信
			sendData();
		});

		//--------------------
		// データ送信
		function sendData() {
			// コメントデータの取得
			const comment = elCmnt.value;
			const len = [...comment].length;
			const lenMax = parseInt(elCmnt.dataset.lenmax);

			// コメントデータの確認
			if (len > lenMax) {
				const msg = `${len}文字です。\n`
					+ `最大文字数${lenMax}より長いです。`;
				alert(msg);
				return;
			}

			//--------------------
			// 画像データの確認
			const time = canvas.getAttribute('time');
			if (time === null) {
				const msg = '画像が読み込まれていません。';
				alert(msg);
				return;
			}

			// 画像データの取得
			const dtUrl = canvas.toDataURL();

			// Base64からバイナリへ変換
			const bin = atob(dtUrl.replace(/^.*?,/, ''));
			const buf = new Uint8Array(bin.length);
			for (let i = 0; i < bin.length; i++) {
				buf[i] = bin.charCodeAt(i);
			}

			// Blobを作成
			const blob = new Blob([buf.buffer], {type: 'image/png'});

			//--------------------
			// 送信用のデータ準備
			const formData = new FormData();
			formData.append('comment', comment);
			formData.append('image', blob);

			// 送信処理
			fetch('/post', {
				method: 'POST',
				body: formData
			})
			.then(response => {
				// サーバーからのレスポンスが異常ならエラーを出す
				if (! response.ok) {
					throw new Error(response);
				}

				// サーバーからのレスポンスが正常ならテキストを返す
				return response.text();
			})
			.then(data => {
				console.log('Success:', data);

				// 表示を更新
				updatePostList();
			})
			.catch(error => {
				console.log('Error:', error);
			});
		}
	});