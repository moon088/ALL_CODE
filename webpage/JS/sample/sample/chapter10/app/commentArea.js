	// windowにDOMContentLoadedの処理を登録
	window.addEventListener('DOMContentLoaded', e => {
		// 要素
		const elCmnt = document.querySelector('#comment');
		const elStat = document.querySelector('#commentStatus');

		//--------------------
		// IME入力時の制御
		let isComposition = false;

		// IME入力開始時の処理
		elCmnt.addEventListener('compositionstart', e => {
			// IME入力中
			isComposition = true;
		});

		// IME入力終了時の処理
		elCmnt.addEventListener('compositionend', e => {
			// IME入力終了
			isComposition = false;

			// コメント入力時の処理
			inputComment();
		});

		// コメント欄、入力時の処理
		elCmnt.addEventListener('input', e => {
			// IME入力時は無視
			if (isComposition) { return; }

			// コメント入力時の処理
			inputComment();
		});

		//--------------------
		// 以降関数

		// コメント入力時の処理
		function inputComment() {
			// 入力情報の取得
			const txt = elCmnt.value;
			const len = [...txt].length;
			const lenMax = parseInt(elCmnt.dataset.lenmax);
			console.log(txt, len);

			// 入力情報の表示
			const cls = len <= lenMax
				? 'inputStatus' : 'inputStatus inputStatusWarn'
			const msg = `<span class="${cls}">`
				+ `（${len}文字 / 最大${lenMax}文字）</span>`;
			elStat.innerHTML = msg;

			// コメントの内容をストレージに保存
			saveStorageComment();
		}
	});