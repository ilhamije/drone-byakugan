import 'leaflet/dist/leaflet.css';

import { Icon } from 'leaflet';
import { MapContainer, Marker, TileLayer, Popup } from 'react-leaflet';
import dronePosition from './images/icon-red-circle-flat.svg'



function MapPlaceholder() {
    return (
        <p>
            Map of London.{' '}
            <noscript>You need to enable JavaScript to see this map.</noscript>
        </p>
    )
}

export default function MapWithPlaceholder() {
    const position = [51.505, -0.09]

    const myIcon = new Icon({
        iconUrl: dronePosition,
        iconSize: [25, 25],
    })

    return (
        <MapContainer
            center={position} zoom={13} scrollWheelZoom={false}
            style={{ height: '100vh' }}
            placeholder={<MapPlaceholder />}>

            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />

            <Marker position={position} icon={myIcon}>

                <Popup>
                    A pretty CSS3 popup. <br /> Easily customizable.
                </Popup>
            </Marker>
        </MapContainer>
    )
}