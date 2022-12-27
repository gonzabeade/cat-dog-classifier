import * as React from 'react';
import './styles.css'; 

const Card = () => {

    const [prediction, setPrediction] = React.useState(0.7)


    const getLabelFromPrediction = (value) => {
        return value > 0.5 ? "dog" : "cat" ;
    } 

    return <div>
            <div className="circle">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/OOjs_UI_icon_upload.svg/1024px-OOjs_UI_icon_upload.svg.png" class="rounded" />
            </div>
            <div className="square">
                <>
                    {!prediction && <p className="label">Upload a picture to classify it.</p>}
                    {
                        prediction && 
                        <div className="labels">
                            <p className="label">Numeric prediction: {prediction}</p>
                            <p className="label">It is a {getLabelFromPrediction(prediction)}!</p>                            
                        </div>
                    }
                </> 

            </div>

    </div>
}
    

export default Card; 