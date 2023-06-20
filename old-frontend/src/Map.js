import { Icon } from 'leaflet';
import { MapContainer, Marker, TileLayer, Popup } from 'react-leaflet';
import dronePosition from './images/icon-red-circle-flat.svg'

import 'leaflet/dist/leaflet.css';


function MapPlaceholder() {
    return (
        <p>
            Drone Photo of Victim in Disaster Area{' '}
            <noscript>You need to enable JavaScript to see this map.</noscript>
        </p>
    )
}

export default function MapWithPlaceholder({ pointData }) {
    const position = [pointData[0].latitude, pointData[0].longitude];

    const myIcon = new Icon({
        iconUrl: dronePosition,
        iconSize: [16, 16],
    })

    return (
        <MapContainer
            center={position} zoom={18} scrollWheelZoom={true}
            style={{ height: '100vh' }}
            placeholder={<MapPlaceholder />}>

            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />

            {pointData &&
                pointData.map((point) => (
                    <Marker position={[point.latitude, point.longitude]}
                        key={point.id}
                        icon={myIcon}>
                        <Popup>
                            Extracted from Image Metadata <br /> File name {point.image_name}
                        </Popup>
                    </Marker>
            ))}
        </MapContainer>
    )
}