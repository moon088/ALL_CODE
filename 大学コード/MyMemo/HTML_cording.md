# HTML全記録
## コーディング
### 全体構造
* 見出し-> \<heading> ~~ </heading\>  
heading1,heading2,heading3で大見出し、中見出し、小見出しに対応(6段階)
* 段落-> \<paragraph> ~~ <paragraph\>
* bodyの中に見出し、見出しh1~h6の中に段落pを入れる
>ex. 
/< `&lt;` 
/> `&gt;`
" `&quot;`
& `&amp;`
© `&copy;`
¥ `&yen;`
* 構造
```html
<html>
    <head>
        <title>(ページのタイトル)</title>
    </head>
    <body>
        (ページ内容)
    </body>
</html>
```
html文章であることを表し、headでページ内容を表す。これは画面表示されない。bodyは画面出力される部分。titileがタイトル

### __属性__
基本的に` <(要素名)　(属性名)=("属性値")>`
* 複数指定可、スペース区切り
* html要素はlnag属性の指定可、要素内の言語の指定 ex.<html lang="ja">
* グローバル属性->どの要素にも指定可 
>id->固有名詞
class->分類名
title->補足情報 
lang->言語

* [__その他の属性リンク__](https://creatorquest.jp/reference/html/global-attributes/)

###　__コンテンツモデル__
#### 配置ルール
* あるカテゴリ内の要素はそのカテゴリに属する要素のみ記述可
* トランスペアレント(透明)は囲まれてる親のコンテンツモデルと同じ
* [__要素リファレンス一覧リンク__](https://creatorquest.jp/reference/html/element/)

####　カテゴリ(コンテンツ)
* メタデータ・コンテンツ->メタデータ、CSS、JSを指定するもの
* フロー・コンテンツ->body要素内なら配置可
* セクショニング・コンテンツ->アウトライン
* ヘディング・コンテンツ->見出し、h1~h6のみ
* フレージング・コンテンツ->ドキュメントのテキスト範囲
* エンベディッド・コンテンツ->外部リソース、多言語によるコンテンツ
* インタラクティブ・コンテンツ->ユーザ操作関連

###　__各タグについて__
#### ul
順不同型リスト。li要素しか挟めない
#### ol
番号付与リスト。li要素しか挟めない
#### li
箇条書き。ul,ol内に配置する
#### dl
用語説明型リスト。dkの中にはdtとddを配置
#### dt
用語内容
#### dd
説明や定義
#### em 
強調表す、`<em> </em>`
#### strong
重要性表す `<strong> </strong>`
#### a
ハイパーリンクの利用。`<a href="リンク先のパス"> (アンカーテキスト) </a>`
トランスペアレント。同じフォルダ内へのリンクは相手のファイル名のみ指定
外部へのリンクはURLをリンク先のパスに指定新しいウィンドウでの表示は<a `href="path" target="_blank"></a>`
#### id
ページ内の違う箇所へのリンクの際、リンク先要素に固有名詞指定
    `<(要素名) id = "固有の名前">~~~</(要素名)>`
    `<a href="#リンク先に指定した固有の名前"></a>`
#### img
画像の埋め込み。src属性を使って参照
    `<img src="表示したい画像ファイルまでのパス" alt="代替テキスト">`
    代替テキストとはうまく出力できない際の出力や、音声読み上げでの読み上げ対象
    前行でリンク指定すれば画像クリックでページ遷移も可能
    `<img src="path" width="px単位で" height="px" alt="代替文字">`
    1px=約0.26mm,100px=2.6cmd
#### table
##### tr
表の行
##### th
表の見出しのセル
##### td
表の内容のセル
```html
<table>
    <thead>
        <tr>
        <th>名前</th>
        <th>職種</th>
        </tr>
    </thead>  
    <tbody>  
        <tr>
            <td>ボブ</td>
            <td>Webディレクター見習い</td>
        </tr>
    </tbody>    
</table>  
```
#### border
デザイン目的でないことを示す
`<table border="空or1">`
#### thead
表のヘッダ
#### tbody
表の内容
#### tfoot
表のフッタ

#### form
フォームの作成、送信先と送信方法をaction,getで指定
`<form action="送信先" method="get (初期値)　/ post">`
#### get
サイト内検索などの検索キーワードの入力
#### post
送信するための入力フォーム
#### input
`<input type="部品の種類" name="部品の名前 value="初期値/送信されるデータ/ボタンのラベル">`
のほかtext,password,radio,checkbox,file,image,reset,submit,buttonがある
checkboxで選択肢で属性揃える
#### textarea
感想などの入力フォーム
`<textarea name="部品の名前" colos="１行当たりの文字数" rows="表示する行数"></textarea>`
#### selec
セレクトボックス
```html
<select name="部品の名前">
<option value="選択肢の属性名">~~<\option>
<\select>
```




## HTML ルール
* コメントアウト　-> `<!-- ~~ -->`
* 改行 -> `<br>`
* js,css読込み -> head内に  
```html
<link rel="~~" href="~~">,<script src="~~></script>
```
で読み込む
* すべてに共通して段落、改行、空白など文法に沿ってコードを書く。デザインに関してはCSSでやる
* コード省略-> heading1をh1,paragraphをp1で省略可
* 文字化け->HTMLcode内の文字コードをHTMLタグで指定すれば文字化け起こらない  
 head要素内に<meta>タグ用いて追記。
 metaタグは要素内容がないので終了タグ不要　
ex. <meta charset="UTF-8">　(Shift_JIS,EUC-JP ect...)
* インデント型ではない(ただちゃんとコーディングする)
* Chromeでサイト開いて検証するとHTMLとCSSのコード見れる
* 2022最新HTML Living Standard(XHTML) (2021から、それまではhtml5)
* DOCTYPE宣言でバージョン指定->この宣言ないと、互換モード。CSSのデザイン崩れる可能性有。宣言有で標準準拠モード
* 最新バージョンのコーディングなら指定しなくてもいいがCSSとのリンクのため宣言するべき
```html
ex.
<!DOCTYPE html>
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN"
"http://www.w3.org/TR/html4/frameset.dtd">
```


## 関連リンク
* [HTML Lesson](https://creatorquest.jp/lessons/)
