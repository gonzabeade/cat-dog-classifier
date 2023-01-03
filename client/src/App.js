import logo from './logo.svg';
import './App.css';
import Card from './components/Card';

function App() {
  return (
    <div className="App">
      <header className="App-header">     
        <p>Cat-Dog Classifier Project</p>
        <Card>
          
        </Card>
        <a href="https://github.com/gonzabeade/cat-dog-classifier">
          <img  className="github-logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png"></img>
        </a>
      </header>
    </div>
  );
}

export default App;
