from bs4 import BeautifulSoup
import requests

#Put the url about your playlist
url = 'https://www.youtube.com/playlist?list=PLNYeagcf77NqE9w2hYJ997UABaDS1L_ge'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#$x('//div/h3/a/text()').map(x=>x.wholeText)


#use here in console browser
urlLibrarySongs = 'https://music.youtube.com/library/songs'

const playButtonElements = document.querySelectorAll('ytmusic-play-button-renderer');
const songList = Array.from(playButtonElements).map(playButtonElement => {
  const ariaLabel = playButtonElement.getAttribute('aria-label');
  const [_, songInfo] = ariaLabel.match(/Reproducir (.+)/);
  const [songName, artist] = songInfo.split(' - ');
  return { songName: songName.trim(), artist: artist.trim() };
});
console.log(songList);
