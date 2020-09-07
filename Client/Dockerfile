FROM node:12

# Create app directory
WORKDIR /client

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json /client/

RUN npm install

# Bundle app source
COPY . /client

CMD npm run serve

EXPOSE 8080