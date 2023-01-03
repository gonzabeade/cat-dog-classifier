import * as React from 'react';
import './styles.css'; 
import axios from 'axios'; 

const Card = () => {

    const [prediction, setPrediction] = React.useState(0.7)
    const [imageURL, setImageURL] = React.useState(null)
    const [image, setImage] = React.useState(null)



    const getLabelFromPrediction = (value) => {
        return value > 0.5 ? "dog" : "cat" ;
    } 

    const handleChange = (e) => {
        setImageURL(URL.createObjectURL(e.target.files[0])); 
        setImage(e.target.files[0])
    }

    const handleSubmit = (e) => {
        let formData = new FormData(); 
        console.log(typeof(image))
        formData.append('file', image); 
        axios.post("http://localhost:8080/images", formData); 
        e.preventDefault(); 
    }

    return <div>
            <div className="square">
                    <input type="file" onChange={handleChange}/>
                    <button onClick={handleSubmit}>Submit</button>
                {imageURL && <img className="uploaded-photo" src={imageURL}></img>}

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