import face from './assets/face.png'

function Card() {
    return (
        <div className="card">
            <img className="card-image" src={face} alt='werhtert'></img>
            <h2 className="card-title"> John</h2 >
            <p className="card-text">moving electrons</p>
        </div >
    );
}

export default Card