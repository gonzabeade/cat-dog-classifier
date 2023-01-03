import * as React from 'react';
import './styles.css'; 
import axios from 'axios'; 

const Card = () => {

    const [prediction, setPrediction] = React.useState(0.7)
    const [image, setImage] = React.useState(null)


    const getLabelFromPrediction = (value) => {
        return value > 0.5 ? "dog" : "cat" ;
    } 

    const handleChange = (e) => {
        setImage(URL.createObjectURL(e.target.files[0]))
    }

    const handleSubmit = (e) => {
        const formData = new FormData(); 
        console.log(image); 
        formData.append('image', image, image.name); 
        axios.post("http://localhost:8080/", formData); 
    }

    return <div>
            <div className="square">
                <form onSubmit={handleSubmit}>
                    <input type="file" onChange={handleChange}/>
                    <button type="submit">Submit</button>
                </form>
                <img className="uploaded-photo" src={image}></img>

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