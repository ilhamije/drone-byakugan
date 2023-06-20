# Use an official node runtime as a parent image
FROM node:latest

RUN mkdir -p /app/node_modules && chown -R node:node /app

# set working directory
WORKDIR /app

# To handle 'not get uid/gid'
RUN npm config set unsafe-perm true

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
ADD package.json /app/package.json
RUN npm install --silent
RUN npm install react-scripts@0.9.5 -g --silent

# start app
CMD ["npm", "start"]
