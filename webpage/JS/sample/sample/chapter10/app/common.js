	// windowにDOMContentLoadedの処理を登録
	window.addEventListener('DOMContentLoaded', e => {
		// ボタンの全要素
		document.querySelectorAll('button')
		.forEach(el => {
			// クリック時のイベント登録
			el.addEventListener('click', e => {
				// フォーカスを解除
				setTimeout(() => {
					el.blur();
				}, 100);
			});
		});
	});