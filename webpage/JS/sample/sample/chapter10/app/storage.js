	// windowにDOMContentLoadedの処理を登録
	window.addEventListener('DOMContentLoaded', e => {
		// Canvasの内容をストレージから復帰
		restoreStorageCanvas();

		// コメントの内容をストレージから復帰
		restoreStorageComment();
	});

	//--------------------
	// キー
	const keyCanvas = 'appCanvas';
	const keyCmnt   = 'appComment';

	//--------------------
	// Canvasの内容をストレージに保存
	function saveStorageCanvas() {
		// 要素の選択
		const canvas = document.querySelector('#view');

		// Data URLの取り出し
		const dtUrl = canvas.toDataURL();

		// ストレージに保存
		localStorage.setItem(keyCanvas, dtUrl);
	}

	// Canvasの内容をストレージから復帰
	function restoreStorageCanvas() {
		// ストレージから取得
		const dtUrl = localStorage.getItem(keyCanvas);
		if (dtUrl === null) { return; }

		// 要素の選択
		const canvas = document.querySelector('#view');
		const context = canvas.getContext('2d');

		// 画像の読み込み
		const img = new Image();
		img.onload = () => {
			// 画像の描画
			context.drawImage(img, 0, 0);

			// 読み込み時間の設定
			canvas.setAttribute('time', Date.now());

			// 表示の変更
			const elNoView = document.querySelector('#noView');
			elNoView.style.display = 'none';
			canvas.style.display = 'inline';
		};
		img.src = dtUrl;
	}

	// Canvasの内容をストレージから削除
	function removeStorageCanvas() {
		// ストレージから削除
		localStorage.removeItem(keyCanvas);
	}

	//--------------------
	// コメントの内容をストレージに保存
	function saveStorageComment() {
		// 要素の選択
		const elCmnt = document.querySelector('#comment');

		// ストレージに保存
		localStorage.setItem(keyCmnt, elCmnt.value);
	}

	// コメントの内容をストレージから復帰
	function restoreStorageComment() {
		// ストレージから取得
		let txt = localStorage.getItem(keyCmnt);
		if (txt === null) { txt = '' }

		// 要素の選択
		const elCmnt = document.querySelector('#comment');

		// デフォルト値の設定
		const txtDefault = elCmnt.dataset.default;
		if (txt === '') { txt = txtDefault }

		// 値の復帰
		elCmnt.value = txt;
	}

	// コメントの内容をストレージから削除
	function removeStorageComment() {
		// ストレージから削除
		localStorage.removeItem(keyCmnt);
	}