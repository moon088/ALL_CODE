	// windowにDOMContentLoadedの処理を登録
	window.addEventListener('DOMContentLoaded', e => {
		// 表示を更新
		updatePostList();
	});

	//--------------------
	// 表示を更新
	function updatePostList() {
		// 要素の選択
		const elPost = document.querySelector('#postListArea');

		// 受信処理
		fetch('/get')
		.then(response => {
			// サーバーの稼働状況によってエラーを出す
			if (!response.ok) {
				throw new Error(response);
			}

			// 正常にサーバーからレスポンスが得られたとき
			return response.json();
		})
		.then(data => {
			console.log('Success:', data);

			// 要素内部を全て削除
			while(elPost.firstChild){
				elPost.removeChild(elPost.firstChild);
			}

			// 表示
			data.list.forEach(x => {
				// 日付表示を作成
				const dateStr = dateFormat(
					'YYYY年MM月DD日 hh時mm分ss秒',
					new Date(x.date));

				// HTMLを作成
				const html = `
<div class="postListItem">
  <div class="plImage">
    <img src="/${x.dir}${x.image}">
  </div>
  <div class="plBody">
    <div class="plComment">
      ${x.comment}
    </div>
    <div class="plDate">
      ${dateStr}
    </div>
  </div>
</div>
				`.trim();

				// 要素を作成して追加
				const el = document.createElement('div');
				el.classList.add('postListItemWrap');
				el.innerHTML = html;
				elPost.appendChild(el);
			});
		})
		.catch(error => {
			console.log('Error:', error);
		});
	}